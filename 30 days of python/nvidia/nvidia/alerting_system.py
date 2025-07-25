import time
from collections import defaultdict

class Alert:
    def __init__(self, tenant, labels, severity, message, timestamp=None):
        self.tenant = tenant
        self.labels = labels
        self.severity = severity
        self.message = message
        self.timestamp = timestamp or time.time()
        self.acknowledged = False

class AlertingSystem:
    def __init__(self):
        self.routing_rules = defaultdict(list)  # tenant -> list of rules
        self.escalation_policies = defaultdict(list)  # tenant -> list of escalation steps
        self.alerts = []  # all alerts
        self.groups = defaultdict(list)  # (tenant, group_key) -> list of alerts

    def add_routing_rule(self, tenant, rule):
        self.routing_rules[tenant].append(rule)

    def set_escalation_policy(self, tenant, policy):
        self.escalation_policies[tenant] = policy

    def ingest_alert(self, alert):
        self.alerts.append(alert)
        group_key = (alert.tenant, tuple(sorted(alert.labels.items())))
        self.groups[group_key].append(alert)
        self.route_alert(alert)

    def route_alert(self, alert):
        # Find matching rules for tenant
        for rule in self.routing_rules[alert.tenant]:
            if rule(alert):
                print(f"Routing alert for {alert.tenant}: {alert.message}")

    def escalate(self, alert):
        # Escalate if not acknowledged
        policy = self.escalation_policies[alert.tenant]
        for step in policy:
            if not alert.acknowledged:
                print(f"Escalating alert to {step}: {alert.message}")

    def deduplicate(self, window=60):
        now = time.time()
        deduped = []
        seen = set()
        for alert in self.alerts:
            key = (alert.tenant, tuple(sorted(alert.labels.items())), alert.severity, alert.message)
            if key not in seen and now - alert.timestamp < window:
                deduped.append(alert)
                seen.add(key)
        return deduped

    def correlate(self):
        # Simple correlation: group by host or service
        correlated = defaultdict(list)
        for alert in self.alerts:
            key = alert.labels.get('host') or alert.labels.get('service')
            if key:
                correlated[key].append(alert)
        return correlated

# Example usage
if __name__ == "__main__":
    system = AlertingSystem()
    # Add a routing rule: route all critical alerts to oncall@example.com
    system.add_routing_rule("tenant1", lambda a: a.severity == "critical")
    # Set escalation policy
    system.set_escalation_policy("tenant1", ["oncall@example.com", "manager@example.com"])
    # Ingest alerts
    system.ingest_alert(Alert("tenant1", {"host": "db1"}, "critical", "DB down"))
    system.ingest_alert(Alert("tenant1", {"host": "db1"}, "critical", "DB down"))
    # Deduplicate
    print("Deduped:", [a.message for a in system.deduplicate()])
    # Correlate
    print("Correlated:", {k: [a.message for a in v] for k, v in system.correlate().items()}) 