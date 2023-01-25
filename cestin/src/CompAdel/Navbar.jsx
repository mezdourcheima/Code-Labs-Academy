import bellIcone from '../assets/images/bell.svg'
import userIcone from '../assets/images/userIcone.png'

const Navbar = () => {
  return (
    <nav className='flex justify-end gap-x-4 w-full rounded py-3 items-center bg-white'>
        <img src={bellIcone} alt="notification bell icone" />
        <img src={userIcone} alt="user account icone" className='mr-12'/>
    </nav>
  )
}

export default Navbar