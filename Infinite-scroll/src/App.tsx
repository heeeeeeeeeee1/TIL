import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

import "./App.css";
import MovieList from "./components/MovieList";

const App = () => {
  const queryClient = new QueryClient();

  return (
    <QueryClientProvider client={queryClient}>
      <MovieList />
    </QueryClientProvider>
  );
};

export default App;
