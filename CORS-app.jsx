import React , {useState , useEffect} from 'react' ;

const App = () => {
    const [data , setData] = useState(null);

    return (
        <div style={{padding:"20px"}}>
            <h1>API DATA</h1>
            {
                data ? (
                    <p>Message : {data.message} </p>
                ) : (
                    <p>
                        Loading...
                    </p>
                )
            }
        </div>
    )
}