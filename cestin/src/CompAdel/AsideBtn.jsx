
const AsideBtn = ({text, icone}) => {
  return (
    <button className="p-1 w-4/5 py-2 flex gap-x-3 items-center text-[#3E619B] bg-white rounded hover:text-white hover:bg-red-600 active:bg-red-600">
        <img src={icone} alt="icone" /><span className="">{text}</span>
    </button>
  )
}

export default AsideBtn