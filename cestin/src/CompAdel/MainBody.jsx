import Navbar from "./Navbar"
import Main from './Main'



const MainBody = () => {
  return (
    <div className="flex flex-col justify-start w-5/6 border rounded">
      <Navbar/>
      <Main/>
    </div>
    
  )
}

export default MainBody