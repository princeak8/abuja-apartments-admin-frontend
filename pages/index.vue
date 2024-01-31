<template>
  <div class="mx-auto border-2 border-red-100">
    <div class="flex border-2">
      <div class="flex-1">
        <img src="/images/landing.jpg" width="100%" alt="landing page image" class="object-cover" />
      </div>
      <div class="flex-1">
        <Card class="w-[350px]">
          <CardHeader>
            <CardTitle>Create project</CardTitle>
            <CardDescription>Deploy your new project in one-click.</CardDescription>
          </CardHeader>
          <CardContent>
            <form>
              <div class="grid items-center w-full gap-4">
                <div class="flex flex-col space-y-1.5">
                  <Label for="name">Name</Label>
                  <Input id="name" placeholder="Name of your project" />
                </div>
                <div class="flex flex-col space-y-1.5">
                  <Label for="framework">Framework</Label>
                  <Select>
                    <SelectTrigger id="framework">
                      <SelectValue placeholder="Select" />
                    </SelectTrigger>
                    <SelectContent position="popper">
                      <SelectItem value="nuxt">
                        Nuxt.js
                      </SelectItem>
                      <SelectItem value="next">
                        Next.js
                      </SelectItem>
                      <SelectItem value="sveltekit">
                        SvelteKit
                      </SelectItem>
                      <SelectItem value="astro">
                        Astro
                      </SelectItem>
                    </SelectContent>
                  </Select>
                </div>
              </div>
            </form>
          </CardContent>
          <CardFooter class="flex justify-between px-6 pb-6">
            <Button variant="outline">
              Cancel
            </Button>
            <Button>Deploy</Button>
          </CardFooter>
        </Card>
      </div>
    </div>
  </div>
</template>
