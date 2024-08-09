Fish Baiter
===========

Project Overview
----------------

Fish Baiter is a system designed to track compromised ATMs across the UK and identify those affected by the Fish Bandit. 
The project leverages real-time data to provide a comprehensive monitoring and issue resolution platform.

Goal
----

The primary objective is to develop a solution for real-time tracking and visualization of affected ATMs, enabling efficient resolution of issues and predicting future activities of the Fish Bandit.

Requirements
------------

-   Real-time tracking of ATM status and locations
-   Interactive dashboard for monitoring ATM data
-   Customer engagement platform for issue resolution
-   Visualization of affected and unaffected ATMs on a map
-   Efficient handling of real-time data and asynchronous updates

Solution
--------

### Architecture

-   **Backend:** Flask
-   **Frontend:** Bootstrap
-   **Real-time Data Streaming:** json-server
-   **Data Storage:** MongoDB
-   **Map Visualization:** Google Maps API
-   **Distance Computation:** Nearest Neighbor algorithm

### Map Integration

The map visualization is powered by the Google Maps API, providing an interactive display of ATM locations. Key features include:

-   **Real-Time Markers:** Display affected and unaffected ATMs with dynamic updates.
-   **Data Loading:** Integrate map data using the Google Maps API to render multiple markers.
-   **Asynchronous Updates:** Utilize asynchronous requests to track and update the status of compromised ATMs in real-time.

Lessons Learned
---------------

1.  **Routing Challenges:** Integrating Flask with JavaScript for seamless routing was complex and required careful handling.
2.  **Map Visualization:** Implementing Google Maps API for dynamic visualization of ATM statuses presented significant challenges but was successfully addressed.
3.  **Real-Time Tracking:** Managing real-time updates and asynchronous requests proved crucial for accurate and timely data representation.

Future Development
------------------

-   **Route Planner Enhancements:** Improve the route planner for customer engineers by incorporating predictive analytics to forecast the Fish Bandit's movements.
-   **Pattern Analysis:** Develop advanced algorithms to analyze patterns and predict future compromise locations.
-   **Long-Term Tracking:** Address challenges associated with tracking compromised ATMs over extended periods.
