import arcade

class Country():

    def __init__(self, map_img_path):
        self.background = None
        self.window.set_mouse_visible(True)
        self.background = arcade.load_texture(map_img_path)
        self.NA_countries = ["United States", "Canada", "Mexico", "Cuba", "Haiti", "Dominican Republic", "Jamaica", "Guatemala", "Belize", "El Salvador",
         "Honduras", "Nicaragua", "Costa Rica", "Panama"]
        self.SA_countries = ["Colombia", "Venezuela", "Guyana", "Suriname", "French Guiana", "Ecuador", "Peru", "Bolivia", "Brazil", "Chile", "Argentina",
         "Uruguay", "Paraguay"]
        self.EU_countries = ["Iceland", "Norway", "Sweden", "Finland", "Estonia", "Latvia", "Lithuania", "Russia", "Belarus", "Ukraine", "Poland", "Denmark",
         "Germany", "Netherlands", "Belgium", "Luxembourg", "France", "Switzerland", "Portugal", "Spain", "United Kingdom", "Ireland", "Italy", "Czechia", 
         "Slovakia", "Austria", "Slovenia", "Croatia", "Hungary", "Serbia", "Romania", "Moldova", "Bulgaria", "Bosnia", "Montenegro", "Albania", "Greece", 
         "Turkey", "Cyprus", "Andorra", "Lieachtenstein", "North Macedonia", "Kosovo"]
        self.AFRICA_countries = ["Morocco", "Algeria", "Tunisia", "Libya", "Egypt", "Western Sahara", "Mauritania", "Mali", "Niger", "Chad", "Sudan", "Eritrea", 
         "Senegal", "Gambia", "Guinea-Bissau", "Guinea", "Sierra Leone", "Liberia", "Cote d'lvoire", "Burkina", "Ghana", "Togo", "Benin", "Nigeria", "Cameroon", 
         "Central African Republic", "South Sudan", "Djibouti", "Ethiopia", "Somalia", "Equatorial Guinea", "Gabon", "Republic of the Congo", "Democratic Republic of the Congo", 
         "Uganda", "Kenya", "Rwanda", "Burundi", "Tanzania", "Angola", "Zambia", "Malawi", "Mozambique", "Zimbabwe", "Namibia", "Botswana", "South Africa", 
         "Lesotho", "Eswatini", "Madagascar", "Sao Tome and Principe"]
        
        
