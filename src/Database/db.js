import mongoose from 'mongoose'
import 'dotenv/config'

const connectDB = async() => {
    try{
        const connectionInstance = await mongoose.connect(`${process.env.MongoDB_URI}`)
        console.log(`Connected to: ${connectionInstance.connection.host}`)
    }
    catch(error){
        console.log("Error occured: ",error)
        process.exit(1)
    }
}
export default connectDB