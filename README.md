# BIG BEN

A discord bot that spams "BONG" for every 30 seconds. Inspired by telegram Bot Big Ben

Heroku configs are attached for easy cloud deployment

## TODO

- Detailed bot setup instruction
- Command Line support
  - /info command to display number of messages bot displayed
  - /schedule \[message\] \[interval\] \[OPTIONAL: start_time\] \[channel_id\] command to task bot to send message 
    starting at user designated time in user designated intervals.
  - /list command to view bot tasks with task id.
  - /remove \[id\] to remove the task corresponding to the id.
  - /classic \[channel\] that adds a custom BONG task, for which it sends message "BONG BONG BONG..." in the channel 
    every hour, for which the number of BONGS depend on current hour in London Time. (e.g. "BONG" at 1:00 AM/PM London,
    "BONG BONG BONG" at 3:00 AM/PM)
- Unit tests
