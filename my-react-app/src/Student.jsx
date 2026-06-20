import {userState} from "react";
function application()
{
    const [info , setInfo] = useState({

        name:"",
        email:"",
        gender:"",
        dob:"",
        skills:""
        

    });

       const [image , setimage]= useState(null);
       const [age , setAge ]=useState (0);
       const change = (e)=> {

         const {name , value} = e.target;
         setInfo ({ 
              ...info,[name]:value
         });

       };
       const skillchange=(e)=>{
            const {value , checked} = e.target;
            if(checked)
            {    setInfo({
                ...info,skills:[...info.skills , value]
             });}
            else 
            {

            }
       };

}
export default Application;