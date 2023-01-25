import AsideBtn from "./AsideBtn"
import Logo from "../assets/images/logo.png"
import edtIcone from '../assets/images/edt.png'
import homeIcone from '../assets/images/home.svg'
import Icone from '../assets/images/Union.png'

const Aside = () => {
  return (
    <div className="flex flex-col gap-y-7 w-1/6 items-center bg-white border rounded">
      <img src={Logo} alt="logo G-Estin" className="justify-start w-4/5 border border-black"/>
      <AsideBtn text='Accueil' icone={homeIcone}/>
      <span className="text-gray-400 w-4/5">Gestion</span>
      <AsideBtn text='EDT' icone={edtIcone}/>
      <AsideBtn text='CP' icone={Icone}/>
      <AsideBtn text='Enseignement' icone={Icone}/>
      <AsideBtn text='Deliberation' icone={Icone}/>
    </div>  
  )
}

export default Aside