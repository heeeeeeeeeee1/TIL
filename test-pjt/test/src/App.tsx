import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import Signup from './pages/signup'; 
import "./App.css";

const queryClient = new QueryClient()

function App() {
  return (

    <QueryClientProvider client={queryClient}>
      <Signup/>
      <ReactQueryDevtools initialIsOpen={false} />
    </QueryClientProvider>
  
  );
}

export default App;
