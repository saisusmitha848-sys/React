import { useEffect } from "react";
function Data(){
   useEffect(
      ()=>{
        console.log("good moring");
      },[]
    );
    return(
        <h1>Good morning</h1>
    )
}
export default Data;