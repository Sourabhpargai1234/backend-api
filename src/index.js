import { app } from './app.js'
import connectDB from './Database/db.js'
import 'dotenv/config'
const PORT = process.env.PORT || 5000

connectDB()
.then(() => {
    app.on("error", (error) => {
        console.log("Caught error: ",error);
        throw error
    })
    app.listen(PORT, ()=> {
        console.log(`Running on ${PORT}`);
    })
})
.catch((error) => {
    console.log(`Error while running server on port: ${port}`)
})
