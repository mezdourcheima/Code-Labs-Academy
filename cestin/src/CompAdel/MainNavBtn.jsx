const MainNavBtn = ({text, color}) => {
    return (
      <button className={`w-full text-[#FFF] bg-[${color}] rounded`}>
          {text}
      </button>
    )
  }
  
  export default MainNavBtn