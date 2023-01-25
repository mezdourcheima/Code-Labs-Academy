import Form from "./Form"
import ConnectHeader from "./ConnectHeader"
const FormCard = () => {
  return (
    <div className="bg-white w-1/2 flex flex-col items-start p-10 border-r-2 border-[#42506B]">
        <ConnectHeader />
        <Form placeHolder="votre e-mail" color='gray' htmlFor='email' inputType='email'/>
    </div>
  )
}

export default FormCard