# Data Observability

## Metrics
- **Data Availability**: Metrics such as Time to Live and Refresh Rate are crucial for data availability.

## Teams
- Teams need to master the necessary technology to build and run data pipelines, utilize reporting tools, and understand business KPIs.

## Producing Value in a Data Project
- A systematic development process is essential to move data into production and make it available for analysis.

## Common Data Issues
- **Regulatory**: Changes in data privacy or other regulations may necessitate adjustments in data collection, ingestion, or storage, potentially leading to unforeseen issues.
- **Business Demand**: Different business use cases may require varied data configurations.
- **Human Error**.
- **Latent Information Error**: Misinterpretation of data can lead to errors. For example, sales of blue sneakers might drop due to a strike affecting stock replenishment, causing buyers to purchase brown ones instead. Market teams, unaware of the underlying issue, might wrongly conclude that brown is the new popular color, leading to unsold inventory once blue sneakers become available again post-strike.
- **Data Drift Errors**: Engineers might not realize the implications of changes made to data, often discovered only at the end of the value chain.

## Areas of Observability
- **Infrastructure**: Log metrics can provide insights into the performance characteristics of internal components.
- **Applications**: Metrics like application endpoint, versions, number of requests, and open threads can help assess application performance.
- **User/Purpose**: Monitoring who is using or implementing the applications.
- **Analytics**: Observing analytics, from simple transformations to complex AI models, aids in identifying and learning from ongoing usage and insights.
- **Security**.

## Definition
Data Observability is the ability of an organization to maintain broad visibility over its data landscape and multi-layer data dependencies (data pipelines, infrastructure, applications) at all times. This capability helps to identify, control, prevent, escalate, and remediate data outages rapidly, adhering to acceptable data SLAs.

## Leveraging Data Observability
- **Low Latency Data Issues Detection**.
- **Efficient Data Issues Troubleshooting**.
- **Preventing Data Issues**.
- **Decentralized Data Quality Management**.
- **Complementing Existing Data Governance Capabilities**.

## Channels of Data Observability Information
Channels that convey observability information to the user:
- **Logs**
- **Metrics**
- **Traces**

## Data Sources and Physical Space
Data sources are linked to servers where they are accessible with the aim to maximize overall interpretability for an external observer. This includes providing a common language that can be used independently of the people, time, and technologies involved.

### Physical Space
- **Servers**
- **Users**
  - Data Users
  - Data Consumers

### Static Space
- **Link Event**: About data to things that can be accessed.

### Data Source
- **Data Source**: Information on what data exists and how it can be used.

### Schema
- **Schema**: Provides visibility into the structure of the data.

### Lineage
- **Lineage**: Tracks the origin and evolution of data within the system.
