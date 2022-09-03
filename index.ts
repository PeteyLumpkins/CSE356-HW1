import express, { Application, Request, Response } from 'express';
import path from "path";

const app: Application = express();
const port: number = 3000;

app.use("/", express.static(path.join(__dirname, "public")));

app.use("/", (req: Request, res: Response): void => {
    res.status(200).redirect("/hw1.html");
});

app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});