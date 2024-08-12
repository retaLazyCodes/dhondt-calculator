export default function NewListButton({setLists, lists}) {
    const INITIAL_VOTES = 0

    const addList = () => {
        setLists([...lists, { name: `Lista #${lists.length + 1}`, votes: INITIAL_VOTES }]);
    };
    
    return (
        <button onClick={addList} className="mt-6 p-2 border rounded-md">
            Nueva Lista
        </button>
    );
}
