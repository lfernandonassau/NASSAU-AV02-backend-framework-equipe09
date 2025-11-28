function Header() {

    return (
        <header className="fixed top-0 left-0 w-full bg-blue-900 text-white p-4 flex justify-between items-center">
            <div>
                <h1 className="font-bold text-xl">GoConsig</h1>
            </div>
            <div className="flex space-x-4">
                <ul>
                    <li><a className="bg-white text-blue-900 px-4 py-1 font-bold rounded hover:text-blue-500 transition duration-500" href="/login">Login</a></li>
                </ul>
                <ul>
                    <li><a className="bg-white text-blue-900 px-4 py-1 font-bold rounded hover:text-blue-500 transition duration-500" href="/register">Registrar</a></li>
                </ul>
            </div>
        </header>
    )
}

export default Header;