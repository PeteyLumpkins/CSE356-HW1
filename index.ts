import express, { Application, Request, Response } from 'express';
import path from "path";

const app: Application = express();
const port: number = 3000;

app.use("/", express.static(path.join(__dirname, "public")));

app.use("/", (req: Request, res: Response): void => {
    res.status(200).sendFile(path.join(__dirname, "/index.html"));
});

app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});