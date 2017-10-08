<pre>
<code class="language-php">public function treeView(){       
        $Categorys = Category::where('parent_id', '=', 0)-&gt;get();
        $tree='&lt;ul id="browser" class="filetree"&gt;&lt;li class="tree-view"&gt;&lt;/li&gt;';
        foreach ($Categorys as $Category) {
             $tree .='&lt;li class="tree-view closed"&lt;a class="tree-name"&gt;'.$Category-&gt;name.'&lt;/a&gt;';
             if(count($Category-&gt;childs)) {
                $tree .=$this-&gt;childView($Category);
            }
        }
        $tree .='&lt;ul&gt;';
        // return $tree;
        return view('files.treeview',compact('tree'));
    }
    public function childView($Category){                 
            $html ='&lt;ul&gt;';
            foreach ($Category-&gt;childs as $arr) {
                if(count($arr-&gt;childs)){
                $html .='&lt;li class="tree-view closed"&gt;&lt;a class="tree-name"&gt;'.$arr-&gt;name.'&lt;/a&gt;';                  
                        $html.= $this-&gt;childView($arr);
                    }else{
                        $html .='&lt;li class="tree-view"&gt;&lt;a class="tree-name"&gt;'.$arr-&gt;name.'&lt;/a&gt;';                                 
                        $html .="&lt;/li&gt;";
                    }
                                   
            }
            
            $html .="&lt;/ul&gt;";
            return $html;
    }    </code></pre>

<p>&nbsp;</p>
