echo %1
cd %1
dotnet build
dotnet publish --configuration Release -o ./Publish
cd Publish
del publish.zip
powershell Compress-Archive ./*.* publish.zip
