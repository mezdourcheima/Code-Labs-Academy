import Input from './Input'
import MainNavBtn from "./MainNavBtn"

const MainNav = ({titre, spanText}) => {
  return (
    <nav className='flex w-full justify-between h-fit'>
        <div className='w-1/4'>
            <h1 className='text-xl'>Comite pedagogique</h1>
            <span className='text-blue-600'>deja existant</span>
        </div>
        <div className=' w-3/4 flex justify-between items-center'>
            <Input />
            <Input />
            <div className='flex flex-col justify-between gap-y-2 '>
                <MainNavBtn text='ajouter' color='#3E619B'/>
                <MainNavBtn text='enregistrer' color='#3E619B'/>
            </div>
        </div>
        
    </nav>
  )
}

export default MainNav