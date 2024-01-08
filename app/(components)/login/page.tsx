import React from 'react'

const login = () => {
    return (
        <>
            <div className='container h-screen mx-auto border-2 border-black'>
                <div className='flex flex-col h-3/4 items-center justify-center border-2 border-black'>
                    <div className="">
                        <h1>Hi there!</h1>
                        <h2>Log in to NeurJAM</h2>
                    </div>

                    <div>
                        <form>
                            <div>
                                <label htmlFor="email">Email</label>
                                <input type="email" name="email" id="email" className='border-2 border-black' />
                            </div>

                            <div>
                                <label htmlFor="password">Password</label>
                                <input type="password" name="password" id="password" className='border-2 border-black' />
                            </div>

                            <div>
                                <p>Do not have an account? <a href="/signup">Sign up here</a></p>
                            </div>

                            <a href="#_" className="relative inline-flex items-center justify-center p-4 px-5 py-3 overflow-hidden font-medium text-indigo-600 rounded-lg shadow-2xl group">
                                <span className="absolute top-0 left-0 w-40 h-40 -mt-10 -ml-3 transition-all duration-700 bg-red-500 rounded-full blur-md ease"></span>
                                <span className="absolute inset-0 w-full h-full transition duration-700 group-hover:rotate-180 ease">
                                    <span className="absolute bottom-0 left-0 w-24 h-24 -ml-10 bg-purple-500 rounded-full blur-md"></span>
                                    <span className="absolute bottom-0 right-0 w-24 h-24 -mr-10 bg-pink-500 rounded-full blur-md"></span>
                                </span>
                                <span className="relative text-white">Login</span>
                            </a>
                        </form>
                    </div>
                </div>
            </div>
        </>
    )
}

export default login