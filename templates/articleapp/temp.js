


temp_html = `
                        <div class="timeline-item-description">
                            <i class="avatar | small">
                                <img src="https://assets.codepen.io/285131/hat-man.png"/>
                            </i>
                            <span><a href="#"> ${username} </a>   작성된 날짜 <time
                                    datetime="20-01-2021"> ${date} </time>
                                    <button class="comment_delete_btn" onclick="delete_comment(${pk})">삭제하기</button>
                            </span>
                        </div>
                        <div class="comment">
                            <p>
                                ${content}
                            </p>
                        </div>`

                $('#comment_content2').append(temp_html)