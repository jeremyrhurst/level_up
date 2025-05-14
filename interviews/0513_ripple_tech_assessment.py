"""
Food delivery companies employ tens of thousands of delivery drivers who each submit hundreds of deliveries per week.
Delivery details are automatically sent to the system immediately after the delivery.

Delivery drivers have different hourly payment rates, depending on their performance.
Drivers can take on, and be paid for, multiple deliveries simultaneously.

If a driver is paid $10.00 per hour, and a delivery takes 1 hour and 30 minutes, the driver is paid $15.00 for that delivery.

We are building a dashboard to show a single number - the total cost of all deliveries - on screens in the accounting department offices.

At first, we want the following functions:

* `add_driver(driver_id [integer], usd_hourly_rate [float])`
   - The given driver will not already be in the system

* `record_delivery(driver_id [integer], start_time, end_time)`
   - Discuss the time format you choose
   - Times require minimum one-second precision
   - The given driver will already be in the system
   - All deliveries will be recorded immediately after the delivery is completed
   - No delivery will exceed 3 hours

* `get_total_cost()`
   - Return the total, aggregated cost of all drivers' deliveries recorded in the system
   - For example, return 135.30 if one driver is in the system and has a total cost of 100.30 USD and another driver is in the system and has a total cost of 35.00 USD.
   - This will be used for a live dashboard
   - Do not worry about exact formatting

All inputs will be valid.

Share any decisions or assumptions you make.
If you do anything differently in this interview than you would in production, share that.

Before coding, let's discuss how you will store the time data and why.

We want to see good OOP practices.
You may look up syntax using a search engine, as long as you are sharing your screen.
"""

"""
The analytics team uses the live dashboard reporting function you built to see how much money is owed in total to all drivers.

Add the following functions:

* `pay_up_to (pay_time: datetime)`
   - Pay all drivers for recorded deliveries which ended up to and including the given time

* `get_total_cost_unpaid()`
   - Return the total, aggregated cost of all drivers' deliveries which have not been paid

The solution does not need to be thread-safe or handle concurrency.
"""

# add driver
# add driver
# record_delivery
# get_total_cost
# { driver_id: {hourly_rate: 20, deliveries: [[start,end], [start,end]]}}
# total_cost: 
from datetime import datetime

class deliveries():
    def __init__(self):
        self.total_cost = 0
        self.drivers = {}
        self.paid = 0
        
    def time_diff(self, start, end):
        difference = end - start
        return(difference.total_seconds() / 3600)
        
    def pay_up_to(self, time):
        # iterate through drivers and through deliveries and pay from start time to current time given
        # update paid
        for driver in self.drivers.values():
            for start, end in driver['deliveries']:
                if time > start:
                    if time >= end:
                        diff = self.time_diff(start, end)
                    # else:
                    #     diff = self.time_diff(start, time)
                        self.paid += diff * driver['usd_hourly_rate']
        return
    
    def get_total_cost_unpaid(self):
        return(self.total_cost - self.paid)
    
    def add_driver(self, driver_id, hourly_rate):
        # returns true when success
        # returns false if already exists
        if driver_id not in self.drivers:
            new_driver = {'usd_hourly_rate': hourly_rate, 'deliveries': []}
            self.drivers[driver_id] = new_driver
            return True
        return False
            
        
    def record_delivery(self, driver_id, start_time, end_time):
        # add to our devlieries
        self.drivers[driver_id]['deliveries'].append((start_time, end_time))
        
        # update total_cost
        rate = self.drivers[driver_id]['usd_hourly_rate']
        # get difference between datetime objects
        hours_difference = self.time_diff(start_time, end_time)
        # multiply hours to rate
        new_cost = hours_difference * rate
        # update total cost
        self.total_cost += new_cost
        
        return
    def get_total_cost(self):
        return(self.total_cost)
        
deliv = deliveries()
deliv.add_driver(1, 35.10)
deliv.add_driver(2, 15.15)
deliv.add_driver(3, 8.55)
deliv.add_driver(4, 11.28)
deliv.record_delivery(1,
    datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0),
    datetime(year=1970, month=1, day=1, hour=1, minute=0, second=0))
deliv.record_delivery(2,
    datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0),
    datetime(year=1970, month=1, day=1, hour=1, minute=30, second=0))
deliv.record_delivery(2,
    datetime(year=1970, month=1, day=1, hour=1, minute=30, second=0),
    datetime(year=1970, month=1, day=1, hour=2, minute=0, second=0))
deliv.pay_up_to(datetime(year=1970, month=1, day=1, hour=1, minute=0, second=0))
print(f'total cost: {deliv.get_total_cost_unpaid()}')
print(f'total cost: {deliv.get_total_cost()}'