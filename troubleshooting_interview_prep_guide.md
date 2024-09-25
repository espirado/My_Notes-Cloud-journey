
# Troubleshooting Interview Preparation Guide

## What to Expect
This interview will take the form of a "story", where you will be given a high-level configuration to explore. You will then be provided with a new issue that has arisen in the system, which you will need to resolve using your practical experience and insights from your exploration.

## What Do We Look For?
The goal is to understand how you:
- Reason about problems
- Apply your skills and knowledge to investigate production issues
- Attempt to root cause and mitigate issues at scale

Issues may span a wide range of areas, including application, server, and network. Do not be discouraged if you have limited familiarity in some areas. The intent is to gauge your breadth of skills and experience across the stack, while also showcasing your strengths.

## Interview Structure
- **Duration**: 45 minutes
- **Format**: Verbal/conversational style
- **Tool**: CoderPad.io (may be used for sharing relevant information)

## Interview Dynamics
The interviewer might present a system-related issue or problem in the infrastructure and ask you to troubleshoot it. They will be interested in the investigative steps you take and the reasoning behind your actions. Use your past experiences and tooling knowledge to:
- Discover what entities are causing problems
- Understand why they are causing problems
- Determine a scalable, preventive solution

### Example Exchange:
**Interviewer**: "You're seeing this in the infrastructure. How would you troubleshoot it?"  
**Interviewee**: "What do I have access to?"  
**Interviewer**: "At least SSH access to the virtual machines, but not necessarily host access."  
**Interviewee**: "I'd try to use the tool `foo` to see what actions our service is taking. I’d look for patterns like `bar` because often when using virtual machines, the observed issue is related to this resource."  
**Interviewer**: "OK, you’ve discovered what entity/resource is causing us problems, but how do we know why?"

### Example Scenarios:
- A service you support is no longer responding to requests
- Your metrics indicate sporadic issues impacting user experience
- An application terminates unexpectedly after a period of time for unknown reasons
- An alert shows a sustained latency regression
- User reports suggest your service has an outage, but your team hasn’t received any alerts
- A production host gets shut down occasionally due to out of memory (OOM)
- A small subset of users experiences surprisingly slow responses

## Additional Tips
- **Structured Approach**: Narrow down potential issues systematically as you zero in on the root cause. Bisect the problem space to rule out potential causes. Be detailed in your investigative methodology using industry-standard tools/methods or any custom setup you are familiar with.
- **Tool Knowledge**: Be prepared to discuss the tools you would use, the specific information they would provide, and the types of issues they would suggest.
- **Data Analysis**: If unsure about a tool, talk about the data you seek and how you would query and review it.
- **Clarification**: Don't hesitate to ask for clarification. The interviewer may be vague to test your ability to operate in ambiguity.
- **Mitigation**: Share multiple ways to mitigate the issue, along with their advantages and disadvantages.
- **Expertise Boundaries**: Clearly state where your expertise starts and ends.
- **Assumptions**: Clearly state any assumptions about service dashboards or logs existing.

## Study Areas
- **Application Layer**: Service dashboards, application logs, and debugging tools
- **OS Level**: Resource utilization, system-level error logs
- **Network Layer**: Network diagnostics and troubleshooting tools
- **Classic Pathologies**: Resource contention, thrashing, thundering herds, and their mitigations
- **Distributed Systems Concepts**: CAP theorem, containerization
- **Troubleshooting Methodologies**: The USE Method (Utilization, Saturation, and Errors)
- **Scalable Investigation**: Investigating issues at scale across hundreds or thousands of servers

## Review Tools and Concepts
- **Service Dashboards**: Understanding and interpreting metrics and logs
- **Application Logs**: Analyzing logs for error patterns and performance issues
- **Resource Utilization**: CPU, memory, disk, and network utilization metrics
- **System-Level Error Logs**: Identifying and interpreting system errors
- **Network Diagnostics**: Tools like `ping`, `traceroute`, and network analyzers
- **Containerization**: Tools like Docker and Kubernetes
- **Distributed Systems**: Concepts like consistency, availability, partition tolerance

## Practice Resources
- **Mock Interviews**: Practice troubleshooting interviews with peers or mentors
- **Real-World Scenarios**: Work on real-world troubleshooting scenarios
- **Tool Proficiency**: Gain hands-on experience with troubleshooting tools
- **Documentation Review**: Study documentation for tools and methodologies

## Final Thoughts
The goal of this interview is to test your depth and breadth. Be clear where your expertise starts and ends, and systematically approach each problem with a structured methodology. Good luck!
