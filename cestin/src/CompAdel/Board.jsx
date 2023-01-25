import FormCard from "./FormCard"
import DefCard from "./DefCard"
const Board = () => {
  return (
    <div class="flex w-full justify-center items-center h-screen bg-[#42506B]">
      <div class="flex w-2/3 justify-center items-center bg-white">
        <FormCard />
        <DefCard />
      </div>
    </div>
  )
}

export default Board