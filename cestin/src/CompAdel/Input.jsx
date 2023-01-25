
const Input = ({label, htmlFor, placeHolder, inputType, inputClassNames, labelClassNames, value}) => {
  return (
    <>
        {label && <label htmlFor={htmlFor} className={labelClassNames}>{label}</label>}
        <input type={inputType} name="" id={htmlFor} className={`form-input rounded-md ${inputClassNames}`} placeholder={placeHolder} value={value}/>
    </>
    
  )
}

export default Input
