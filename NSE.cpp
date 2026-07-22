#include <iostream>
#include <string>
#include <cmath>
#include <fstream>
#include <sstream>
#include <set>
#include <vector>
#include <filesystem>
const double PI = 3.14159265358979323846;
using namespace std;

struct Airport {
    string ident;
    string type;
    string name;
    int elevation_ft;
    string continent;
    string iso_country;
    string iso_region;
    string municipality;
    string icao_code;
    string iata_code;
    string gps_code;
    string local_code;
    double longitude;
    double lat;   
};
 
double Hav(const vector<Airport>& a, int response3, int response4){
    double change_in_lat = a[response4].lat - a[response3].lat;
    double change_in_lon = a[response4].longitude - a[response3].longitude;
    double haversine = pow(sin(change_in_lat/2), 2) + cos(a[response3].lat) * cos(a[response4].lat) * pow(sin(change_in_lon/2), 2);
    haversine = haversine * (PI/180);
    haversine = haversine * 6371;
    return haversine;
}


void printer (const Airport &a){
    cout << "===============================" << endl;
    cout << "Ident: " << a.ident << endl;
    cout << "Type: " << a.type << endl;
    cout << "Name: " << a.name << endl;
    cout << "Elevation (ft): " << a.elevation_ft << endl;
    cout << "Continent: " << a.continent << endl;
    cout << "ISO Country: " << a.iso_country << endl;
    cout << "ISO Region: " << a.iso_region << endl;
    cout << "Municipality: " << a.municipality << endl;
    cout << "ICAO Code: " << a.icao_code << endl;
    cout << "IATA Code: " << a.iata_code << endl;
    cout << "GPS Code: " << a.gps_code << endl;
    cout << "Local Code: " << a.local_code << endl;
    cout << "Coordinates: " << a.longitude << ", " << a.lat << endl;
}

void Distance(const vector<Airport>& a){
    set <string> coutries;  
    for (int i = 1; i < a.size(); i++){
        coutries.insert(a[i].iso_country);
    }
    cout << "Select two airporst you want to calculate the distance between: " << endl;
    cout << "Countries: " << endl;
    int counter = 0;
    for (const string& country : coutries){
        cout << counter << ". " << country <<endl;
        counter++;
    }
    cout << "Enter the number corresponding to the first  country: " << endl;
    int response1;
    cin >> response1;
    while (response1 < 0 || response1 >= coutries.size()){
        cout << "Invalid input. Please enter a number between 0 and " << coutries.size() - 1 << "." << endl;
        cin.clear();
        cin.ignore(1000, '\n');
    }
    cout << "Enter the number corresponding to the second  country: " << endl;
    int response2;
    cin >> response2;
    while (response2 < 0 || response2 >= coutries.size()){
        cout << "Invalid input. Please enter a number between 0 and " << coutries.size() - 1 << "." << endl;
        cin.clear();
        cin.ignore(1000, '\n');
    }
    for (int i = 1; i < coutries.size(); i++){
        if (a[i].iso_country == *next(coutries.begin(), response1)){
            cout << i<< "\t";
            printer(a[i]);
            
        }
    }
     for (int i = 1; i < a.size(); i++){
        if (a[i].iso_country == *next(coutries.begin(), response2)){
            cout << i<< "\t";
            printer(a[i]);
            
        }
    }
    cout << "Enter the number corresponding to the first airport: " << endl;
    int response3;
    while (response3 < 0 || response3 >= a.size()){
        cout << "Invalid input. Please enter a number between 0 and " << a.size() - 1 << "." << endl;
        cin.clear();
        cin.ignore(1000, '\n');
    }
     cout << "Enter the number corresponding to the second airport: " << endl;
    cin >> response3;
    while (response3 < 0 || response3 >= a.size()){
        cout << "Invalid input. Please enter a number between 0 and " << a.size() - 1 << "." << endl;
        cin.clear();
        cin.ignore(1000, '\n');
    }
    cout << "Enter the number corresponding to the second airport: " << endl;
    int response4;
    cin >> response4;
    while (response4 < 0 || response4 >= a.size()){
        cout << "Invalid input. Please enter a number between 0 and " << a.size() - 1 << "." << endl;
        cin.clear();
        cin.ignore(1000, '\n');
    }
    a[response3].longitude;
    a[response3].lat;
    a[response4].longitude;
    a[response4].lat;
    double change_in_lat = a[response4].lat - a[response3].lat;
    double change_in_lon = a[response4].longitude - a[response3].longitude;
    double haversine = pow(sin(change_in_lat/2), 2) + cos(a[response3].lat) * cos(a[response4].lat) * pow(sin(change_in_lon/2), 2);
    haversine = haversine * (PI/180);
    haversine = haversine * 6371;
    cout << "Distance between " << a[response3].name << " and " << a[response4].name << ": " << haversine << " km" << endl;
    
}
Airport new_records(const vector<Airport>& airports){
    Airport new_airport;
    cout << "Enter the following details for the new airport:" << endl;
    cout << "Ident: ";
    cin >> new_airport.ident;
    cout << "Type: ";
    cin >> new_airport.type;
    cout << "Name: ";
    cin.ignore();
    getline(cin, new_airport.name);
    cout << "Elevation (ft): ";
    cin >> new_airport.elevation_ft;
    cout << "Continent: ";
    cin >> new_airport.continent;
    cout << "ISO Country: ";
    cin >> new_airport.iso_country;
    cout << "ISO Region: ";
    cin >> new_airport.iso_region;
    cout << "Municipality: ";
    cin.ignore(); 
    getline(cin, new_airport.municipality);
    cout << "ICAO Code: ";
    cin >> new_airport.icao_code;
    cout << "IATA Code: ";
    cin >> new_airport.iata_code;
    cout << "GPS Code: ";
    cin >> new_airport.gps_code;
    cout << "Local Code: ";
    cin >> new_airport.local_code;
    cout << "Longitude: ";
    cin >> new_airport.longitude;
    cout << "Latitude: ";
    cin >> new_airport.lat;
    
    return new_airport;
}
void sorter(const vector<Airport>& airports){
    multiset<string> countries;
    for (const Airport& a : airports) {
        countries.insert(a.iso_country);
    }

    multiset<string> names;
    for(const Airport& a : airports) {
        names.insert(a.name);
    }
    multiset<string> types;
    for(const Airport& a : airports) {
        types.insert(a.type);
    }
    multiset<string> elevations;
    for(const Airport& a : airports) {
        elevations.insert(to_string(a.elevation_ft));
    }
    multiset<string> longitudes;
    for(const Airport& a : airports) {
        longitudes.insert(to_string(a.longitude));
    }
    multiset<string> latitudes;
    for(const Airport& a : airports) {
        latitudes.insert(to_string(a.lat));
    }
switch(1){
    case 1:
    cout << "Airports sorted by country:" << endl;
    for (const string& country : countries) {
        cout << country << endl;
    }
    break;
    case 2:
    cout << "Airports sorted by name:" << endl;
    for (const string& name : names) {
        cout << name << endl;
    }
    break;
    case 3:
    cout << "Airports sorted by type:" << endl;
    for (const string& type : types) {
        cout << type << endl;
    }
    break;
    case 4:
    cout << "Airports sorted by elevation:" << endl;
    for (const string& elevation : elevations) {
        cout << elevation << endl;
    }
    break;
    case 5:
    cout << "Airports sorted by longitude:" << endl;
    for (const string& longitude : longitudes) {
        cout << longitude << endl;
    }
    break;
    case 6:
    cout << "Airports sorted by latitude:" << endl;
    for (const string& latitude : latitudes) {
        cout << latitude << endl;
    }
    break;
    default:
    cout << "Invalid choice. Please enter a number between 1 and 6." << endl;
    break;

}}
void Searching(const vector<Airport>& airports, int response){
    cin.ignore(1000, '\n'); 
    string air;
    switch(response){
        case 1:
            cout << "Enter the country name of the airport you want to search for: " << endl;
            getline(cin, air);
            while(!(cin >> air)){
                cout << "Invalid input. Please enter a valid country name." << endl;
                cin.clear();
                cin.ignore(1000, '\n');
            }
            cout << "Airport found: " << endl;
            for (int i = 0; i < airports.size();i++){
        if(airports[i].iso_country == air){
            printer(airports[i]);
        }
    }   
            break;
        case 2:
            cout << "Enter the name of the airport you want to search for: " << endl;
            getline(cin, air);
            while (!(cin >> air)){
                cout << "Invalid input. Please enter a valid airport name." << endl;
                cin.clear();
                cin.ignore(1000, '\n');
            }
             cout << "Airport found: " << endl;
            for (int i = 0; i < airports.size();i++){
            if(airports[i].name == air){
            printer(airports[i]);
        }
    }   
        break;
        case 3:
        cout << "Enter the IATA code of the airport you want to search for: " << endl;
        getline(cin, air);
        while (!(cin >> air)){
            cout << "Invalid input. Please enter a valid IATA code." << endl;
            cin.clear();
            cin.ignore(1000, '\n');
        }
        cout << "Airport found: " << endl;
            for (int i = 0; i < airports.size();i++){
        if(airports[i].iata_code == air){
            printer(airports[i]);
        }
    }
        break;
        default:
        cout << "Invalid choice. Please enter a number between 1 and 3." << endl;
        return;}      }
 
    void csv_Saver(const string& filename, const Airport& a){
    ofstream file(filename, ios::app);
    if (!file.is_open()) {
        cout << "Error: Could not open CSV file for writing." << endl;
        return;
        file << a.ident << "," << a.type << "," << a.name << "," << a.elevation_ft << "," << a.continent << "," << a.iso_country << "," << a.iso_region << "," << a.municipality << "," << a.icao_code << "," << a.iata_code << "," << a.gps_code << "," << a.local_code << ",\"" << a.longitude << "," << a.lat <<"\""  << endl;
        file.close();
    }
    }
    
    void data_analysis(const vector<Airport>& airport){
        int max_elevation = 0;
        int min_elevation = 0;
        for (int i =0; i < airport.size(); i++){
            if (airport[i].elevation_ft > max_elevation) { 
                max_elevation = i;
            }
            if (airport[i].elevation_ft < min_elevation) {
                min_elevation = i;
            }
        }  cout << "Airport with the highest elevation: " << endl;
         printer(airport[max_elevation]);
            cout << endl <<"Airport with the lowest elevation: " << endl << endl;
        printer(airport[min_elevation]);
        int count = 0;
        for (int i = 0; i < airport.size(); i++){
            if (airport[i].iata_code.empty()){
                count++;
            }
        }
        cout << "Airports with missing IATA codes: " << count << endl;
    }

void csv_Loader(vector<Airport>& airports){
    ifstream file("c:/Users/andee/Project1/NSE_airport_program/Airports1.csv");
    if (!file.is_open()) {
        cout << "Error: Could not open CSV file." << endl;
        return ;
    }
string line;
int count = 0;
getline(file, line);
while (getline(file, line)) {
    stringstream ss (line);
    string op;
    string temp;
    string temp2;
    Airport a;
    try{
    getline(ss, a.ident, ',');
    getline(ss, a.type, ',');
    getline(ss, a.name, ',');
    getline(ss, op, ',');a.elevation_ft = stoi(op);
    getline(ss, a.continent, ',');
    getline(ss, a.iso_country, ',');
    getline(ss, a.iso_region, ',');
    getline(ss, a.municipality, ',');
    getline(ss, a.icao_code, ',');
    getline(ss, a.iata_code, ',');
    getline(ss, a.gps_code, ',');
    getline(ss, a.local_code, ',');
    getline(ss, temp2, '"'); 
    getline(ss, temp2, '"');
    stringstream coords(temp2);
    string Lonstr,Latstr;
    getline(coords, Lonstr, ',');
    getline(coords, Latstr, ',');
    a.longitude = stod(Lonstr);
    a.lat = stod(Latstr);
    }
    catch(...){
    }
    airports.push_back(a);
    count++;
}
    file.close();
};
int main() {
    vector<Airport> airports;
    csv_Loader(airports);
    cout << "***************************" << endl;
    cout << "\t Nottingham SkyRoute Explorer" << endl << endl;
    cout << "1. Search for Airports" << endl;
    cout << "2. Calculate Distance between two Airports" << endl;
    cout << "3. Add new record" << endl;
    cout << "4. Data Analysis" << endl;
    cout << "5. Exit" << endl;
    cout << "Enter your choice: " << endl;

    int choice;
    while(!(cin >> choice)){
        cout << "Invalid input. Please enter a number between 1 and 5." << endl;
        cin.clear();
        cin.ignore(1000, '\n');
    }
    switch (choice){
        case 1:
            cout << "Select How you want to search for airports: " << endl;
            cout << "1. Search by country" << endl;
            cout << "2. Search by name" << endl;
            cout << "3. Search by IATA code" << endl;
            int response;            
            while(!(cin >> response)){
                cout << "Invalid input. Please enter a number between 1 and 3." << endl;
                cin.clear();
                cin.ignore(1000, '\n');
            }
            Searching(airports,response);
            main();
                   
            //Searching();
            break;
        case 2:
                Distance(airports);
                main();
            
            break;
        case 3:
            airports.push_back(new_records(airports));
            csv_Saver("c:/Users/andee/Project1/NSE_airport_program/Airports1.csv", airports.back()); 
            main();
            
            break;
        case 4:
            data_analysis(airports);
            main();
            break;
        case 5:
            exit(0);
            break;
        default:
            cout << "Invalid choice. Please enter a number between 1 and 5." << endl;
            main();
            break;
    }
    return 0;
}
