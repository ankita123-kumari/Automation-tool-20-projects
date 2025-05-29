import datetime

class MeetingScheduler:
    def __init__(self, working_hours=(9, 17)):
        self.schedule = {}  # Stores meetings for each date
        self.working_hours = working_hours  # Default: 9 AM to 5 PM

    def is_available(self, date, start_time, end_time):
        """Check if the time slot is available."""
        if date not in self.schedule:
            return True  # No meetings on this date yet

        for meeting in self.schedule[date]:
            if not (end_time <= meeting[0] or start_time >= meeting[1]):
                return False  # Overlapping meeting found

        return True

    def schedule_meeting(self, date, start_time, end_time):
        """Schedule a meeting if the slot is available."""
        if start_time < self.working_hours[0] or end_time > self.working_hours[1]:
            print("Meeting time is outside working hours!")
            return False

        if self.is_available(date, start_time, end_time):
            self.schedule.setdefault(date, []).append((start_time, end_time))
            print(f"Meeting scheduled on {date} from {start_time}:00 to {end_time}:00")
            return True
        else:
            print("Time slot is already booked!")
            return False

    def view_schedule(self, date):
        """View scheduled meetings for a given date."""
        if date in self.schedule:
            print(f"Meetings on {date}:")
            for meeting in self.schedule[date]:
                print(f"- {meeting[0]}:00 to {meeting[1]}:00")
        else:
            print(f"No meetings scheduled on {date}.")

# Example Usage
scheduler = MeetingScheduler()
scheduler.schedule_meeting("2025-05-30", 10, 11)
scheduler.schedule_meeting("2025-05-30", 12, 13)
scheduler.view_schedule("2025-05-30")