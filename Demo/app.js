const express = require("express");
const cors = require("cors");
const fs = require("fs");
const app = express();
const path = "/Users/liu/Desktop/南信大/大数据/视频"; // 电影目录的路径

app.use(
    cors({
        origin: "*",
    })
);

app.get("/movies", (req, res) => {
    fs.readdir(path, (err, files) => {
        if (err) {
            console.error(err);
            return res.status(500).send("Error reading directory");
        }

        const movieList = files.filter((file) => file.endsWith(".wmv"));
        res.json(movieList);
    });
});

app.listen(3000, () => {
    console.log("Server is running on port 3000");
});
