<pre>
<code class="language-php"> public function autosuggest()
    {
        $keyword = Input::get('query');
        $keyword = preg_replace('/[^A-Za-z0-9\ ]/', '', $keyword) ;
        $suggestions = SearchIndex::select('searchable_type', 'searchable_id','priority', 'item_title', 'item_description',
            DB::raw('(match (keywords) against (\'' . $keyword . '\')) as score'),
            DB::raw('(match (item_title) against (\'' . $keyword . '\')) as score2')
        )
            -&gt;whereRaw('match (keywords) against (\'' . $keyword . '\')')
            -&gt;orWhereRaw('match (item_title) against (\'' . $keyword . '\')')
        
            -&gt;orderBy(DB::raw('score+score2*2'), 'desc')
            -&gt;take(20)
            -&gt;get();
        return return View::make('home.index', compact('suggestions'));
    }</code></pre>

<p>&nbsp;</p>
