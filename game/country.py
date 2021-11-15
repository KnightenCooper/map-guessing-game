import arcade


# This file just holds the list of all of the countries for each continent, class is never constructed/initialized


class Country():

    def __init__(self, map_img_path):
        self.background = None
        self.window.set_mouse_visible(True)
        self.background = arcade.load_texture(map_img_path)
        self.NA_countries = ["United States", "Canada", "Mexico", "Cuba", "Haiti", "Dominican Republic", "Jamaica", "Guatemala", "Belize", "El Salvador",
         "Honduras", "Nicaragua", "Costa Rica", "Panama"] # 14 countries
        self.SA_countries = ["Colombia", "Venezuela", "Guyana", "Suriname", "French Guiana", "Ecuador", "Peru", "Bolivia", "Brazil", "Chile", "Argentina",
         "Uruguay", "Paraguay"] # 13 countries
        self.EU_countries = ["Iceland", "Norway", "Sweden", "Finland", "Estonia", "Latvia", "Lithuania", "Russia", "Belarus", "Ukraine", "Poland", "Denmark", # 12
         "Germany", "Netherlands", "Belgium", "Luxembourg", "France", "Switzerland", "Portugal", "Spain", "United Kingdom", "Ireland", "Italy", "Czechia", # 12
         "Slovakia", "Austria", "Slovenia", "Croatia", "Hungary", "Serbia", "Romania", "Moldova", "Bulgaria", "Bosnia", "Montenegro", "Albania", "Greece", # 13
         "Turkey", "Cyprus", "Andorra", "Liechtenstein", "North Macedonia", "Kosovo"] # 6
        # 43 total countries
        self.AFRICA_countries = ["Morocco", "Algeria", "Tunisia", "Libya", "Egypt", "Western Sahara", "Mauritania", "Mali", "Niger", "Chad", "Sudan", "Eritrea", # 12
         "Senegal", "Gambia", "Guinea-Bissau", "Guinea", "Sierra Leone", "Liberia", "Cote d'lvoire", "Burkina", "Ghana", "Togo", "Benin", "Nigeria", "Cameroon", # 13
         "Central African Republic", "South Sudan", "Djibouti", "Ethiopia", "Somalia", "Equatorial Guinea", "Gabon", "Republic of the Congo", "Democratic Republic of the Congo", #9
         "Uganda", "Kenya", "Rwanda", "Burundi", "Tanzania", "Angola", "Zambia", "Malawi", "Mozambique", "Zimbabwe", "Namibia", "Botswana", "South Africa", # 13
         "Lesotho", "Eswatini", "Madagascar", "Sao Tome and Principe"] # 4
         # 47 total countries
        self.ASIA_countries = ["Russia", "Mongolia", "China", "Kazakhstan", "Turkey", "North Korea", "South Korea", "Japan", "India", "Myanmar", "Saudi Arabia", 
         "Iran", "Indonesia", "Malaysia", "Philippines", "Singapore", "Taiwan", "Georgia", "Armenia", "Azerbaijan", "Turkmenistan", "Uzbekistan", "Kyrgyzstan", 
         "Tajikistan", "Cyprus", "Syria", "Lebanon", "Israel", "Jordan", "Iraq", "Afghanistan", "Kuwait", "Bahrain", "Qatar", "United Arab Emirates", "Yemen", 
         "Oman", "Pakistan", "Nepal", "Bhutan", "Bangladesh", "Sri Lanka", "Laos", "Vietnam", "Cambodia"]
        
        
