Traffic Control
Traffic control (sometimes called traffic routing or traffic shaping) refers to the act of controlling where traffic goes and how it gets there. It’s a necessity when running Kubernetes in production because it allows you to protect your infrastructure and apps from attacks and traffic spikes. Two techniques to incorporate into your app development cycle are rate limiting and circuit breaking.

Use case: I want to protect services from getting too many requests
Solution: Rate limiting

Whether malicious (for example, brute‑force password guessing and DDoS attacks) or benign (such as customers flocking to a sale), a high volume of HTTP requests can overwhelm your services and cause your apps to crash. Rate limiting restricts the number of requests a user can make in a given time period. Requests can include something as simple as a GET request for the homepage of a website or a POST request on a login form. When under DDoS attack, for example, you can use rate limiting to limit the incoming request rate to a value typical for real users.

Use case: I want to avoid cascading failures
Solution: Circuit breaking

When a service is unavailable or experiencing high latency, it can take a long time for incoming requests to time out and clients to receive an error response. The long timeouts can potentially cause a cascading failure, in which the outage of one service leads to timeouts at other services and the ultimate failure of the application as a whole.

Circuit breakers prevent cascading failure by monitoring for service failures. When the number of failed requests to a service exceeds a preset threshold, the circuit breaker trips and starts returning an error response to clients as soon as the requests arrive, effectively throttling traffic away from the service.

Traffic Splitting
Traffic splitting (sometimes called traffic testing) is a subcategory of traffic control and refers to the act of controlling the proportion of incoming traffic directed to different versions of a backend app running simultaneously in an environment (usually the current production version and an updated version). It’s an essential part of the app development cycle because it allows teams to test the functionality and stability of new features and versions without negatively impacting customers. Useful deployment scenarios include debug routing, canary deployments, A/B testing, and blue‑green deployments. (There is a fair amount of inconsistency in the use of these four terms across the industry

Use case: I’m ready to test a new version in production
Solution: Debug routing
   Let’s say you have a banking app and you’re going to add a credit score feature. Before testing with customers, you probably want to see how it performs in production. Debug routing lets you deploy it publicly yet “hide” it from actual users by allowing only certain users to access it, based on Layer 7 attributes such as a session cookie, session ID, or group ID. For example, you can allow access only to users who have an admin session cookie – their requests are routed to the new version with the credit score feature while everyone else continues on the stable version.


Use case: I need to make sure my new version is stable
Solution: Canary deployment
   The concept of canary deployment is taken from an historic mining practice, where miners took a caged canary into a coal mine to serve as an early warning of toxic gases. The gas killed the canary before killing the miners, allowing them to quickly escape danger. In the world of apps, no birds are harmed! Canary deployments provide a safe and agile way to test the stability of a new feature or version. A typical canary deployment starts with a high share (say, 99%) of your users on the stable version and moves a tiny group (the other 1%) to the new version. If the new version fails, for example crashing or returning errors to clients, you can immediately move the test group back to the stable version. If it succeeds, you can switch users from the stable version to the new one, either all at once or (as is more common) in a gradual, controlled migration.


Use case: I need to find out if customers like a new version better than the current version
Solution: A/B testing

  Now that you’ve confirmed your new feature works in production, you might want to get customer feedback about the success of the feature, based on key performance indicators (KPIs) such as number of clicks, repeat users, or explicit ratings. A/B testing is a process used across many industries to measure and compare user behavior for the purpose of determining the relative success of different product or app versions across the customer base. In a typical A/B test, 50% of users get Version A (the current app version) while the remaining 50% gets Version B (the version with the new, but stable, feature). The winner is the one with the overall better set of KPIs.



  Use case: I want to move my users to a new version without downtime
Solution: Blue‑green deployment

   Now let’s say your banking app is due for a major version change…congratulations! In the past, upgrading versions usually meant downtime for users because you had to take down the old version before moving the new version into production. But in today’s competitive environment, downtime for upgrades is unacceptable to most users. Blue‑green deployments greatly reduce, or even eliminate, downtime for upgrades. Simply keep the old version (blue) in production while simultaneously deploying the new version (green) alongside in the same production environment.

Most organizations don’t want to move 100% of users from blue to green at once – after all, what if the green version fails?! The solution is to use a canary deployment to move users in whatever increments best meet your risk‑mitigation strategy. If the new version is a disaster, you can easily revert everyone back to the stable version in just a couple of keystrokes.



You can accomplish advanced traffic control and splitting with most Ingress controllers and service meshes.

