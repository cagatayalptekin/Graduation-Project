Our project consists of a structure that makes code suggestions
using LLM models, allows comparing previously produced codes
according to test results, and also allows users to test the code
they produce in two different languages. In this way, software,
test engineers and all kinds of users will be able to compare
these models and generate code by choosing the model among
the options.


# To run the program:
- The last application was in week_5, download week_5 and go to the week_5 folder using cmd.
- LLM models need to be downloaded to the Models folder in week_5. The links are included in the txt file in this folder. There are 3 models and each is approximately 5 GB in size. 
- Create the virtual environment after downloading:
```bash
virtualenv week_5
```
- Activate virtualenv(windows):
```bash
week_5/scripts/activate
```
- To install the libraries in requirement.txt:
```bash
pip install -r requirement.txt
```
- after downloading the libraries, To run the system:
```bash
streamlit run app.py
```
