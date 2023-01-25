import Input from "./Input"
const Form = () => {
  return (
    <form className="w-4/5 flex flex-col self-center">
        <Input inputType="email" htmlFor="email" label='adresse e-mail' placeHolder={'votre adresse e-mail'} labelClassNames={'text-xs mb-1'}
        inputClassNames={" mb-6 w-full border-gray-400 border text-xxs p-1 px-3"} />
        <Input inputType="password" color={'gray'} htmlFor="mdp" label='mot de passe' placeHolder={'votre mot de passe'} inputClassNames={"mb-4 w-full border-gray-400 p-1 px-3 border text-xxs"} labelClassNames={'text-xs mb-1'}/>
        <Input inputType={'submit'} htmlFor='SIBtn' value='Connecter' inputClassNames={'bg-[#3E619B] text-white text-xs w-3/4 self-center mt-10'}/>
    </form>
  )
}

export default Form