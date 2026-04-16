from datetime import datetime, timedelta

class Solution:
    # slow and fast pointer
    def risingTemperature(self, weather_table):
        # Convert date strings in the input data to datetime objects
        # This allows for easy date arithmetic and sorting.
        for row in weather_table:
            row['recordDate'] = datetime.strptime(row['recordDate'], '%Y-%m-%d')

        # Sort the weather records by date
        # This ensures we process days in chronological order.
        sorted_weather = sorted(weather_table, key=lambda x: x['recordDate'])

        result_ids = []

        # Iterate through the sorted weather data starting from the second day
        # We compare each day with its preceding day.
        for i in range(1, len(sorted_weather)):
            current_day = sorted_weather[i]
            previous_day = sorted_weather[i-1]

            # Check if the current day is exactly one day after the previous day
            is_consecutive_day = (current_day['recordDate'] - previous_day['recordDate']) == timedelta(days=1)

            # If it's the next consecutive day and the temperature increased
            if is_consecutive_day and current_day['temperature'] > previous_day['temperature']:
                result_ids.append({'id': current_day['id']})

        return result_ids
