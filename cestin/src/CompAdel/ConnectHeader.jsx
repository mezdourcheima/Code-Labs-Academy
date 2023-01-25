import React from 'react'

const ConnectHeader = () => {
  return (
    <div className='w-4/5 self-center'>
        <h1 className="text-lg">
            Connexion
        </h1>
        <p className="text-gray-500 text-xs mb-3">
            entrez vos identifiants pour accéder à votre compte
        </p>
        <button className="w-full rounded-md border-gray-400 border text-center p-1 px-3 my-1 text-gray-500 text-sm mb-12 mt-2 text-xxs">
            connectez-vous avec votre compte google
        </button>
    </div>
  )
}

export default ConnectHeader