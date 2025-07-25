import uuid
import time
import threading
from collections import defaultdict

class TraceContext:
    def __init__(self, trace_id=None, parent_id=None):
        self.trace_id = trace_id or str(uuid.uuid4())
        self.span_id = str(uuid.uuid4())
        self.parent_id = parent_id

class Tracer:
    def __init__(self, collector, sample_rate=0.01):
        self.collector = collector
        self.sample_rate = sample_rate

    def start_span(self, name, parent_ctx=None):
        if parent_ctx and parent_ctx.trace_id:
            ctx = TraceContext(trace_id=parent_ctx.trace_id, parent_id=parent_ctx.span_id)
        else:
            ctx = TraceContext()
        sampled = (uuid.uuid4().int % 100) < (self.sample_rate * 100)
        return Span(ctx, name, self.collector, sampled)

class Span:
    def __init__(self, ctx, name, collector, sampled):
        self.ctx = ctx
        self.name = name
        self.collector = collector
        self.start = time.time()
        self.end = None
        self.tags = {}
        self.sampled = sampled

    def set_tag(self, k, v):
        self.tags[k] = v

    def finish(self):
        self.end = time.time()
        if self.sampled:
            self.collector.report(self)

class TraceCollector:
    def __init__(self):
        self.lock = threading.Lock()
        self.traces = defaultdict(list)  # trace_id -> list of spans

    def report(self, span):
        with self.lock:
            self.traces[span.ctx.trace_id].append({
                'span_id': span.ctx.span_id,
                'parent_id': span.ctx.parent_id,
                'name': span.name,
                'start': span.start,
                'end': span.end,
                'tags': span.tags
            })

    def get_trace(self, trace_id):
        return self.traces.get(trace_id, [])

# Example usage
if __name__ == "__main__":
    collector = TraceCollector()
    tracer = Tracer(collector, sample_rate=1.0)  # 100% sampling for demo

    # Simulate a request across 2 services
    root_span = tracer.start_span("api_request")
    time.sleep(0.01)
    db_span = tracer.start_span("db_query", parent_ctx=root_span.ctx)
    time.sleep(0.01)
    db_span.set_tag("db.table", "users")
    db_span.finish()
    root_span.finish()

    print("Trace:", collector.get_trace(root_span.ctx.trace_id)) 