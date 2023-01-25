import MainNav from "./MainNav"

const Main = () => {
  return (
    <main className='w-full h-full flex justify-center items-center rounded'>
        <div className='w-11/12 h-5/6 bg-white rounded-xl p-6'>
            <MainNav/>
        </div>
    </main>
  )
}

export default Main