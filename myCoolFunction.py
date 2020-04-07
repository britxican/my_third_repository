#!/usr/bin/python3

import pdb
# Used in sendRequest and sendRequestUsingNextPageInfo
import requests

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# myCoolFunction
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def MyCoolFunction(query, accstkn, \
        perPageParam = 100, \
        orderParam = 'asc', \
        quals = 'in:file'):

    URL = 'https://api.laCucarachaReloaded.com/search/?q=' + \
        '%22' + query + '%22' + '+' + quals + params 
    
    hdrs = {}
    hdrs['Authorization'] = 'token ' + accstkn
    # ******** CONSIDERATIONS FOR CODE SEARCH ***********
    #
    # At most, search results can show two fragments 
    #    from the same file, but there may be more results 
    #    within the file.
    # You can't use the following wildcard characters 
    #    as part of your search query: 
    #    . , : ; / \ ` ' " = * ! ? # $ & + ^ | ~ < >
    #    ( ) { } [ ]. The search will simply ignore these 
    #    symbols.
    # Only repositories with fewer than 500,000 files 
    #    are searchable.
    # https://help.github.com/en/github/searching-for-information-on-github/searching-code#considerations-for-code-search
    # This method returns up to 100 results per page.
    # Due to the complexity of searching code, there are
    # a few restrictions on how searches are performed:
    #   * Only the default branch is considered. In most 
    #     cases, this will be the master branch.
    #   * Only files smaller than 384 KB are searchable.
    # https://developer.github.com/v3/search/#search-code
    # Limitations: the GitHub Search API provides up 
    # to 1,000 results for each search.
    # https://developer.github.com/v3/search/
    # By default, forks are not shown in search results.
    # You can choose to include them in repository 
    # searches, and in code searches if they meet 
    # certain criteria.
    # Forks are only indexed for code search when they 
    # have more stars than the parent repository. You 
    # will not be able to search the code in a fork 
    # that has less stars than its parent. To show 
    # forks with more stars than the parent repository 
    # in code search results, add fork:true or 
    # fork:only to your query.
    # https://help.github.com/en/github/searching-for-information-on-github/searching-in-forks
    #
    # *********** EXACT MATCHES IMPOSSIBLE *********
    #
    # The search index tries to find natural word 
    # breaks to split at -- like case transitions 
    # (e.g. "FooBarBaz") or non-word characters 
    # (e.g. the hyphen in "jquery-tictactoe").
    # In the first example, "FooBarBaz" would be 
    # broken into the following tokens: foo, bar, 
    # baz, and foobarbaz. Only those words will 
    # be searchable. Searching for foobar will 
    # not find occurrences of "FooBarBaz".
    # In the second example, "jquery-tictactoe" 
    # would be broken into the following tokens: 
    # jquery, tictactoe, and jquery-tictactoe. 
    # So searching tictactoe would match, but 
    # searching tictac would not.
    # Note that the search query itself is only 
    # tokenized on whitespace and punctuation, 
    # not on case transitions like the content 
    # that lives on GitHub. For example, if a
    #  user types "FooBarBaz" in the search bar, 
    # GitHub does not generate foo, bar, and baz 
    # tokens for the search query -- They will 
    # only be searching for the one token 
    # foobarbaz. So they will find occurrences of 
    # FooBarBaz on GitHub, but they won't find 
    # occurrences of FooBar.
    # https://github.community/t5/How-to-use-Git-and-GitHub/Github-Enterprise-How-to-find-files-containing-only-an-exact/td-p/10217
    # Exact matches in code search is in beta for 
    # a limited number of users and repositories 
    # on GitHub, and is subject to change.
    # https://help.github.com/en/github/searching-for-information-on-github/searching-code
    # Users who have been selected for the beta 
    # are now able to search select repositories 
    # by pressing f on the repository page and 
    # entering their desired query.
    # https://github.blog/changelog/2019-11-13-code-search-exact-match-limited-beta/
    # Exact matches in code search is in beta 
    # for a limited number of users and 
    # repositories on GitHub.
    # Searching files within a repository for 
    # exact matches only works with some 
    # repositories. 
    # https://help.github.com/en/github/searching-for-information-on-github/searching-code-for-exact-matches
        
    URL = 'https://api.laCucarachaReloaded.com/search/?q=' + \
        '%22' + query + '%22' + '+' + quals + params 
    
    hdrs = {}
    hdrs['Authorization'] = 'token ' + accstkn
    # ******** CONSIDERATIONS FOR CODE SEARCH ***********
    #
    # At most, search results can show two fragments 
    #    from the same file, but there may be more results 
    #    within the file.
    # You can't use the following wildcard characters 
    #    as part of your search query: 
    #    . , : ; / \ ` ' " = * ! ? # $ & + ^ | ~ < >
    #    ( ) { } [ ]. The search will simply ignore these 
    #    symbols.
    # Only repositories with fewer than 500,000 files 
    #    are searchable.
    # https://help.github.com/en/github/searching-for-information-on-github/searching-code#considerations-for-code-search
    # This method returns up to 100 results per page.
    # Due to the complexity of searching code, there are
    # a few restrictions on how searches are performed:
    #   * Only the default branch is considered. In most 
    #     cases, this will be the master branch.
    #   * Only files smaller than 384 KB are searchable.
    # https://developer.github.com/v3/search/#search-code
    # Limitations: the GitHub Search API provides up 
    # to 1,000 results for each search.
    # https://developer.github.com/v3/search/
    # By default, forks are not shown in search results.
    # You can choose to include them in repository 
    # searches, and in code searches if they meet 
    # certain criteria.
    # Forks are only indexed for code search when they 
    # have more stars than the parent repository. You 
    # will not be able to search the code in a fork 
    # that has less stars than its parent. To show 
    # forks with more stars than the parent repository 
    # in code search results, add fork:true or 
    # fork:only to your query.
    # https://help.github.com/en/github/searching-for-information-on-github/searching-in-forks
    #
    # *********** EXACT MATCHES IMPOSSIBLE *********
    #
    # The search index tries to find natural word 
    # breaks to split at -- like case transitions 
    # (e.g. "FooBarBaz") or non-word characters 
    # (e.g. the hyphen in "jquery-tictactoe").
    # In the first example, "FooBarBaz" would be 
    # broken into the following tokens: foo, bar, 
    # baz, and foobarbaz. Only those words will 
    # be searchable. Searching for foobar will 
    # not find occurrences of "FooBarBaz".
    # In the second example, "jquery-tictactoe" 
    # would be broken into the following tokens: 
    # jquery, tictactoe, and jquery-tictactoe. 
    # So searching tictactoe would match, but 
    # searching tictac would not.
    # Note that the search query itself is only 
    # tokenized on whitespace and punctuation, 
    # not on case transitions like the content 
    # that lives on GitHub. For example, if a
    #  user types "FooBarBaz" in the search bar, 
    # GitHub does not generate foo, bar, and baz 
    # tokens for the search query -- They will 
    # only be searching for the one token 
    # foobarbaz. So they will find occurrences of 
    # FooBarBaz on GitHub, but they won't find 
    # occurrences of FooBar.
    # https://github.community/t5/How-to-use-Git-and-GitHub/Github-Enterprise-How-to-find-files-containing-only-an-exact/td-p/10217
    # Exact matches in code search is in beta for 
    # a limited number of users and repositories 
    # on GitHub, and is subject to change.
    # https://help.github.com/en/github/searching-for-information-on-github/searching-code
    # Users who have been selected for the beta 
    # are now able to search select repositories 
    # by pressing f on the repository page and 
    # entering their desired query.
    # https://github.blog/changelog/2019-11-13-code-search-exact-match-limited-beta/
    # Exact matches in code search is in beta 
    # for a limited number of users and 
    # repositories on GitHub.
    # Searching files within a repository for 
    # exact matches only works with some 
    # repositories. 
    # https://help.github.com/en/github/searching-for-information-on-github/searching-code-for-exact-matches
        
    URL = 'https://api.laCucarachaReloaded.com/search/?q=' + \
        '%22' + query + '%22' + '+' + quals + params 
    
    hdrs = {}
    hdrs['Authorization'] = 'token ' + accstkn
    # ******** CONSIDERATIONS FOR CODE SEARCH ***********
    #
    # At most, search results can show two fragments 
    #    from the same file, but there may be more results 
    #    within the file.
    # You can't use the following wildcard characters 
    #    as part of your search query: 
    #    . , : ; / \ ` ' " = * ! ? # $ & + ^ | ~ < >
    #    ( ) { } [ ]. The search will simply ignore these 
    #    symbols.
    # Only repositories with fewer than 500,000 files 
    #    are searchable.
    # https://help.github.com/en/github/searching-for-information-on-github/searching-code#considerations-for-code-search
    # This method returns up to 100 results per page.
    # Due to the complexity of searching code, there are
    # a few restrictions on how searches are performed:
    #   * Only the default branch is considered. In most 
    #     cases, this will be the master branch.
    #   * Only files smaller than 384 KB are searchable.
    # https://developer.github.com/v3/search/#search-code
    # Limitations: the GitHub Search API provides up 
    # to 1,000 results for each search.
    # https://developer.github.com/v3/search/
    # By default, forks are not shown in search results.
    # You can choose to include them in repository 
    # searches, and in code searches if they meet 
    # certain criteria.
    # Forks are only indexed for code search when they 
    # have more stars than the parent repository. You 
    # will not be able to search the code in a fork 
    # that has less stars than its parent. To show 
    # forks with more stars than the parent repository 
    # in code search results, add fork:true or 
    # fork:only to your query.
    # https://help.github.com/en/github/searching-for-information-on-github/searching-in-forks
    #
    # *********** EXACT MATCHES IMPOSSIBLE *********
    #
    # The search index tries to find natural word 
    # breaks to split at -- like case transitions 
    # (e.g. "FooBarBaz") or non-word characters 
    # (e.g. the hyphen in "jquery-tictactoe").
    # In the first example, "FooBarBaz" would be 
    # broken into the following tokens: foo, bar, 
    # baz, and foobarbaz. Only those words will 
    # be searchable. Searching for foobar will 
    # not find occurrences of "FooBarBaz".
    # In the second example, "jquery-tictactoe" 
    # would be broken into the following tokens: 
    # jquery, tictactoe, and jquery-tictactoe. 
    # So searching tictactoe would match, but 
    # searching tictac would not.
    # Note that the search query itself is only 
    # tokenized on whitespace and punctuation, 
    # not on case transitions like the content 
    # that lives on GitHub. For example, if a
    #  user types "FooBarBaz" in the search bar, 
    # GitHub does not generate foo, bar, and baz 
    # tokens for the search query -- They will 
    # only be searching for the one token 
    # foobarbaz. So they will find occurrences of 
    # FooBarBaz on GitHub, but they won't find 
    # occurrences of FooBar.
    # https://github.community/t5/How-to-use-Git-and-GitHub/Github-Enterprise-How-to-find-files-containing-only-an-exact/td-p/10217
    # Exact matches in code search is in beta for 
    # a limited number of users and repositories 
    # on GitHub, and is subject to change.
    # https://help.github.com/en/github/searching-for-information-on-github/searching-code
    # Users who have been selected for the beta 
    # are now able to search select repositories 
    # by pressing f on the repository page and 
    # entering their desired query.
    # https://github.blog/changelog/2019-11-13-code-search-exact-match-limited-beta/
    # Exact matches in code search is in beta 
    # for a limited number of users and 
    # repositories on GitHub.
    # Searching files within a repository for 
    # exact matches only works with some 
    # repositories. 
    # https://help.github.com/en/github/searching-for-information-on-github/searching-code-for-exact-matches
        
    URL = 'https://api.laCucarachaReloaded.com/search/?q=' + \
        '%22' + query + '%22' + '+' + quals + params 
    
    hdrs = {}
    hdrs['Authorization'] = 'token ' + accstkn
    # ******** CONSIDERATIONS FOR CODE SEARCH ***********
    #
    # At most, search results can show two fragments 
    #    from the same file, but there may be more results 
    #    within the file.
    # You can't use the following wildcard characters 
    #    as part of your search query: 
    #    . , : ; / \ ` ' " = * ! ? # $ & + ^ | ~ < >
    #    ( ) { } [ ]. The search will simply ignore these 
    #    symbols.
    # Only repositories with fewer than 500,000 files 
    #    are searchable.
    # https://help.github.com/en/github/searching-for-information-on-github/searching-code#considerations-for-code-search
    # This method returns up to 100 results per page.
    # Due to the complexity of searching code, there are
    # a few restrictions on how searches are performed:
    #   * Only the default branch is considered. In most 
    #     cases, this will be the master branch.
    #   * Only files smaller than 384 KB are searchable.
    # https://developer.github.com/v3/search/#search-code
    # Limitations: the GitHub Search API provides up 
    # to 1,000 results for each search.
    # https://developer.github.com/v3/search/
    # By default, forks are not shown in search results.
    # You can choose to include them in repository 
    # searches, and in code searches if they meet 
    # certain criteria.
    # Forks are only indexed for code search when they 
    # have more stars than the parent repository. You 
    # will not be able to search the code in a fork 
    # that has less stars than its parent. To show 
    # forks with more stars than the parent repository 
    # in code search results, add fork:true or 
    # fork:only to your query.
    # https://help.github.com/en/github/searching-for-information-on-github/searching-in-forks
    #
    # *********** EXACT MATCHES IMPOSSIBLE *********
    #
    # The search index tries to find natural word 
    # breaks to split at -- like case transitions 
    # (e.g. "FooBarBaz") or non-word characters 
    # (e.g. the hyphen in "jquery-tictactoe").
    # In the first example, "FooBarBaz" would be 
    # broken into the following tokens: foo, bar, 
    # baz, and foobarbaz. Only those words will 
    # be searchable. Searching for foobar will 
    # not find occurrences of "FooBarBaz".
    # In the second example, "jquery-tictactoe" 
    # would be broken into the following tokens: 
    # jquery, tictactoe, and jquery-tictactoe. 
    # So searching tictactoe would match, but 
    # searching tictac would not.
    # Note that the search query itself is only 
    # tokenized on whitespace and punctuation, 
    # not on case transitions like the content 
    # that lives on GitHub. For example, if a
    #  user types "FooBarBaz" in the search bar, 
    # GitHub does not generate foo, bar, and baz 
    # tokens for the search query -- They will 
    # only be searching for the one token 
    # foobarbaz. So they will find occurrences of 
    # FooBarBaz on GitHub, but they won't find 
    # occurrences of FooBar.
    # https://github.community/t5/How-to-use-Git-and-GitHub/Github-Enterprise-How-to-find-files-containing-only-an-exact/td-p/10217
    # Exact matches in code search is in beta for 
    # a limited number of users and repositories 
    # on GitHub, and is subject to change.
    # https://help.github.com/en/github/searching-for-information-on-github/searching-code
    # Users who have been selected for the beta 
    # are now able to search select repositories 
    # by pressing f on the repository page and 
    # entering their desired query.
    # https://github.blog/changelog/2019-11-13-code-search-exact-match-limited-beta/
    # Exact matches in code search is in beta 
    # for a limited number of users and 
    # repositories on GitHub.
    # Searching files within a repository for 
    # exact matches only works with some 
    # repositories. 
    # https://help.github.com/en/github/searching-for-information-on-github/searching-code-for-exact-matches
