## Introduction:
- In the provided code, it’s been tried to design a simple algorithm that  receives addresses as inputs and returns the corresponding country names.

### Current Problem:
- One limitation of the current approach is that this approach cannot handle multi-word cities, such as "Kematen in Tirol," "Breitenbach am Inn," etc. 
In addition, there may be cities with the same name in different countries, and the addresses may contain misspelling problems.

### Experiment Process:
- To improve the current approach, I experimented with different methods. First, I explored the locationtagger library, which can handle multi-word cities and provides accurate results to detect cities and countries. However, it was inefficient and slow. Then, I tried a pre-trained language model, dslim/bert-base-NER.  This model was efficient and fast, but its overall performance was poor, and the main challenge was I didn't have tag labels. Therefore , I just chose the simpler approach, that was efficient and performed better.

### Suggestions for Improvements:

#### Normalization:
- To standardize the address text, a simple normalizer function is used. This process involves converting the text to lowercase, removing diacritics using the Unicode library and normalizing non-ASCII characters to their closest ASCII equivalent, removing digits, and keeping only alphabetic characters and whitespaces. This normalization step helps in handling variations in input addresses.

#### Country Code Mapping:
- Then for efficient lookups based on normalized country names, I used the Pycountry library. I used this library because the names of countries may already be mentioned in the addresses. It provides the name of the country along with its ISO format, which is more efficient than checking the whole data.

#### Handling Multi Word Cities:
- Multiword cities are identified and stored in the multiword_cities set. This helps to consider verification of their presence in the normalized address. In the current dataset, I found a total of 19,919 multiword cities.

#### Main Approach:
- The code follows a two-step process. First, it checks if the name of the country is mentioned in the addresses using Country Code Mapping. If not, it identifies multiword cities by extracting them from the available data. then, it checks these multiword cities in the normalized address along with the associated country data. Finally it looks for the name of cities in the normalized city data.  To handle misspelling, I use Levenshtein distances and consider a Levenshtein distance of 1 or 2 as an exact match if it exists. 
Future Improvement:
In the future, we can use a transformer-based model and use a pretrained model for the task of NER, and use CRF architecture to enhance the algorithm, and  to improve its accuracy further.

## Installation
Please, clone the repository to your local machine:

- git clone https://github.com/RaanaMahdavi/address_to_country_textkernel.git
- cd address_to_country_textkernel
- python setup.py install
- run data_input.py
- run business_logic.py
- run test.py
## Usage
- A test.py file can be found in the adress_to_country
## Using a wheel file
- python setup.py bdist_wheel

### Notes:

- The installation instructions now shows the usage of `setup.py` for installing needed package.


