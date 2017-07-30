# final_project

#Description
[Chowster](https://powerful-brook-42988.herokuapp.com/) is a foodtruck locator application that incorporates the Google Maps API. The app is based off of geolocations from Google Maps, so the truck driver won't have to give a latitude and longitude, but will give an address. The app is split into 2 different interactions, the truck driver or the user. The truck driver sets their location, logo, and menu to show to the user. Once the location is set, the truck's logo will appear on the map. The user will be able to look on the map, or the list of trucks, to find a truck around their location. The map centers around the location of the user so they can see which truck is in their area. The user will be able to rate the different trucks and leave comments about the service. Also if a user gives their email address then they will recieve an email of the truck's new location if the driver chooses to give that location to the users who favorited their truck.

#Features
 - Chowster allows for new users to sign up.
 - After a new account is created they choose what they are between these two options:
  * Truck Driver
    - A truck driver can create new trucks.
    - After the truck is created, they just plug in an address and mark if the truck is on site or not.
    - The driver updates the menu to list the food items that the foodtruck contains.
    - They are allowed to comment on their profile page or other users' profile pages.
  * Customer/User
    - A user can comment on the foodtruck's profile or other account users' profiles.
    - A user can leave a star rating (1-5) of a foodtruck.
    - A user will be able to favorite any foodtruck they want.
 - If the truck is marked as onsite, the icon of the truck's picture (or logo) will be displayed on the map through a Google Maps API geolocation to appear at that exact address.
 - If a user has favorited a truck and they have left their email, when a truck that they have favorited changes locations, the truck driver is given an option to send an email directly to the users of the new location.
 - There is a search engine (through Elasticsearch) to find a truck by searching of these 4 options:
  * Truck Name
  * Truck Driver
  * Food Type
  * Checked In?
 - Once a user is logged in, they can give their location to have the map display their location in the middle to show if any trucks are around in the area.

 #ToDo
  - Set up a time field for drivers so that the trucks will appear or disappear on the map based on the time.
  - Work on texting the users of the location, like the email.
