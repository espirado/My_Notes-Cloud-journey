# Reading List

- [Service Efficient to Automate](https://dancres.github.io/Pages/):  
  Is it what we refer to more generally as operations-friendly? Services that are operations-friendly require little human intervention and both detect and recover from all but the most obscure failures without administrative intervention.

  - **Expect Failures**:  
    A component may crash or be stopped at any time.

  - **Keep Things Simple**:  
    Complexity breeds problems.

  - **Automate Everything**:  
    Focus on reducing manual intervention through automation.

## Operation Process

- **Design for Failure**:  
  The entire service must be capable of surviving failure without human administrative interaction. Failure recovery must be a simple path and tested frequently.

- **Redundancy and Fault Recovery**:  
  Designing a service such that any system can crash (or be brought down for service) at any time while still meeting the service level agreement (SLA) requires careful engineering. The acid test for full compliance with this design principle is: Is the operations team willing and able to bring down any server in the service at any time without hesitation?

### Key Design Considerations

- **Commodity Hardware Slice**
- **Single-Version Software**
- **Multi-Tenancy**
- **Enforce Admission Control at All Levels**
