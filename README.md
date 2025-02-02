# Turkish ID Verifier

## Description
This Python script allows the validation of Turkish ID Numbers by using the [official NVI Public API](https://tckimlik.nvi.gov.tr/service/kpspublic.asmx). It uses SOAP to communicate with the service, sending user-provided information to check the validity of the provided Turkish ID Number. 

The script validates:
- **T.C. Kimlik No** (National ID number)
- **Ad** (First name)
- **Soyad** (Last name)
- **Doğum Yılı** (Year of birth)

## Requirements

The following Python libraries are required to run this script:

- `requests`: For sending HTTP requests.
- `xml.etree.ElementTree`: For parsing the XML response from the API.
- `unicode_tr`: A library to prevent converting 'i' to 'I' in Turkish characters.

To install the required dependencies, use the following:

```bash
pip install requests
pip install unicode_tr
```

## How to Use

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/tc-kimlik-no-dogrulama.git
   ```

2. Navigate to the project directory:

   ```bash
   cd tc-kimlik-no-dogrulama
   ```

3. Run the script using Python:

   ```bash
   python tc_kimlik_dogrulama.py
   ```

4. The script will prompt you for the following information:
   - **T.C. Kimlik No** (National ID Number)
   - **Ad** (First Name)
   - **Soyad** (Last Name)
   - **Doğum Yılı** (Year of Birth)

5. Once the information is entered, the script will attempt to validate the provided T.C. Kimlik Number with the NVI API.

6. You will receive one of the following messages:
   - **"Doğrulama başarılı."** (Validation successful.)
   - **"Doğrulama başarısız. Bilgileri tekrar kontrol ediniz"** (Validation failed. Please check your information.)

## Example

```
TC Kimlik: 12345678901
Ad: Ahmet
Soyad: Yılmaz
Doğum yılı: 1985
```

Output:
```
HTTP Status Code: 200
Doğrulama başarılı.
```

## Error Handling
The script handles SOAP response errors in the form of a failure to return the correct XML element. If an invalid T.C. Kimlik number is entered or there are mismatched details, the script will respond with an error message: `Doğrulama başarısız. Bilgileri tekrar kontrol ediniz`.

## Notes
- The script uses the official SOAP-based web service from the Turkish Government’s NVI system to perform the validation.
- This service is available only for Turkish citizens. Therefore, the input parameters should correspond to valid data in the system.
  
## Potential Improvements
- Add a retry mechanism if the NVI service is temporarily unavailable.
- Improve user input validation for T.C. Kimlik No and other parameters.
- Implement logging for better tracking of requests and responses.
  
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
