lotNumber = "037-00901-00027"
CountryCode = lotNumber[0:3]
ProductCode = lotNumber[4:9]
BatchNumber = lotNumber[-5:]
print("CountryCode = " + CountryCode)
print("ProductCode = " + ProductCode)
print("BatchNumber = " + BatchNumber)
