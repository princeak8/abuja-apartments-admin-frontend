<template>
    <div class="w-full">
        <Navbar />
        <div class="flex flex-row w-full border-1 border-blue-700">
            <div class="flex-initial w-60">
                <SideBar />
            </div>
            <div class="flex-1 pl-3 pr-3 pt-20 ">
                <slot></slot>

                <!-- <h3>Footer</h3> -->
            </div>
            
        </div>
    </div>
</template>