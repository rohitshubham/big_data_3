# Assignment report 3

### CS-E4640 Big data platforms 
#### Rohit Raj ([rohit.raj@aalto.fi](mailto:rohit.raj@aalto.fi)) - 801636
---
## Part 1
###  Design for streaming analytics 

 
1. The dataset used for streaming analytics was the `Indoor Localization Dataset`. The dataset contains information concerning the older people’s movement inside their homes regarding their indoor location in the home setting [1]. This is a time-series data and hence, suitable for streaming analysis and provide real-time time-sensitive updates. 

The dataset contains 4 fields, `part_id`, `ts_date`, `ts_time` and `room`. The fields `ts_date` and `ts_time` gives us the exact timestamp and the field `room` gives us the location where the person entered at that time. According to the dataset providers, it is assumed that the person remained in the same room till the next recoding data.

The two different analytics that a person can do is :
* __Streaming analytics__: The streaming analytics in this type of dataset is very important. The streaming analytics will give us intermediate reports of the person's location. We can run streaming analysis on a tumbling window of a fixed duration where we measure the person's location and flag (and alarm) any suspicion. For example: If an elderly spends more than one hour in kitchen, we can send and alarm to the emergency/health services as it is abnormal to be in kitchen for more than one hour. We can define different threshold for different rooms such as 12 hour for bedroom etc. Hence, a timely report from streaming analytics is necessary. 

* __Batch Analytics__: Batch analytics in this case could run on the result produced in the from the stream analytics. This type of analysis will run on certain fixed intervals (once a day or once a week) and will help us in determining the general trend of an elderly person's health behaviour. We can think of the result from the stream analysis as an input to this batch analysis.  

Therefore, the two broad analysis objectives for this dataset would be `Immediate health monitoring` (Done by streaming analytics) and `long term health monitoring` (Done by batch analysis).

2. The analytics should handle `non-keyed` data-stream in this case. Since, we have seen that the data is linear and contains only one type of information for every user. `Keyed` data streams are useful where one type of producer gives different types of consumer data (And each my require different type of stream processing). Since, our dataset only contains location and timestamp of a user, we need everything to be processed on a single stream-analytics application.

The delivery guarantee for our data should ideally be `exactly-once`. Our stream-analytics is responsible for monitoring the health of elderly using their room movement. A loss of data (even a single message) would trigger a false alarm with the health services. (For example a missed message would lead to the stream-analytics app decide that this elder person hasn't moved from kitchen in 1 hour). Hence, it is extremely imperative that there is no loss of messages. A duplication of data can also lead to wrong analysis that this user has infact moved twice in one hour, where as in reality he hasn't. So a potential health hazard would not be flagged by our stream analysis app in this case.

3. 

---
### References

[1] Ellul J, Polycarpou M, Kotsani M; Indoor Localization Dataset; May 7, 2019;  Available at: https://zenodo.org/record/2671590#.XXJahPxRUlU