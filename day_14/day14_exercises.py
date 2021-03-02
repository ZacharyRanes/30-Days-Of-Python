from functools import reduce

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Use map to create a new list by changing each country to uppercase in the countries list
countries_u = list(map(lambda c: c.upper(), countries))
print(countries)
print(countries_u)

# Use map to create a new list by changing each number to its square in the numbers list
numbers_sq = list(map(lambda n: n ** 2, numbers))
print(numbers)
print(numbers_sq)

# Use filter to filter out countries containing 'land'.
countries_l = list(filter(lambda c: True if 'land' in c else False, countries))
print(countries_l)

# Use filter to filter out countries having exactly six characters.
countries_6 = list(filter(lambda c: True if len(c) == 6 else False, countries))
print(countries_6)

# Use filter to filter out countries containing six letters and more in the country list
countries_l6 = list(filter(lambda c: True if len(c) < 6 else False, countries))
print(countries_l6)

# Use filter to filter out countries starting with an 'E'
countries_n6 = list(filter(lambda c: True if c[0] != 'E' else False, countries))
print(countries_n6)

# Declare a function called get_string_lists which takes a list as a parameter
# and then returns a list containing only string items.
mixed_list = ['String1', 'String2', 3, 'String3']
def get_string_lists(list_in):
    return list(filter(lambda c: True if type(c) is str else False, list_in))
print(get_string_lists(mixed_list))

# Use reduce to sum all the numbers in the numbers list.
numbers_s = reduce(lambda a, b: a + b, numbers)
print(numbers_s)

# Create a function returning a dictionary,
# where keys stand for starting letters of countries
# and values are the number of country names starting with that letter.
def countries_by_fl(country_l):
    country_d = {}
    for c in country_l:
        country_d[c[0]] = country_d.get(c[0], 0) + 1
    return country_d
# I must be doing this a way they do not want but I maybe to slow to pick this up
# need to make this with lambda or map or something

country_fl_dic = countries_by_fl(countries)
for i in country_fl_dic:
    print(i + ' ' + str(country_fl_dic[i]))

