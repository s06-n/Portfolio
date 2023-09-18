const express = require("express");
const path = require("path");

const app = express();
const port = 3000;
 
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "../WEEK 1/CalculatorWebsite.html"));
});

app.listen(port, () => {
    console.log(`app listening on port ${port}`)
})

app.use(express.static(path.join(__dirname, "../WEEK 1/")));