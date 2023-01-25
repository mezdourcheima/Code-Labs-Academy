import Aside from "./Aside"
import MainBody from "./MainBody"

const Frame = () => {
  return (
    <div className="flex w-full h-screen">
        <Aside/>
        <MainBody/>
    </div>
  )
}

export default Frame