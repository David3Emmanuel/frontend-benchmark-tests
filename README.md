# Benchmark Tests for Popular Frontend Tools

benchmark.py was run on all combinations of the following:
* Package Managers:
    * npm
    * yarn
* Build Frameworks:
    * create-react-app
    * vite
    * create-next-app

## Results
See results in [results.json](/results.json)
|Build Tool           |Time Taken (H:MM:SS)|Folder Size|
|---------------------|--------------------|-----------|
|npx create-react-app |0:41:12             |234 MB     |
|yarn create react-app|0:22:55             |146 MB     |
|npm create vite      |0:05:22             |50.6 MB    |
|yarn create vite     |0:03:56             |50.5 MB    |
|npx create-next-app  |0:17:30             |284 MB     |
|yarn create next-app |0:19:43             |254 MB     |
